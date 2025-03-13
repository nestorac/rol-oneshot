function Table(elem)
  -- Función auxiliar para extraer el texto de la caption de forma segura
  local function get_caption_text(caption)
    local text = ""
    if caption then
      if caption.long then
        -- Caso de estructura nueva
        if #caption.long > 0 then
          text = pandoc.utils.stringify(caption.long)
        end
      elseif type(caption) == "table" then
        -- Caso de estructura antigua (o simple lista de inlines)
        if #caption > 0 then
          text = pandoc.utils.stringify(caption)
        end
      end
    end
    return text
  end

  -- Si existe 'headers', usamos la estructura antigua
  if elem.headers then
    local caption = elem.caption
    local aligns = elem.aligns or {}
    local headers = elem.headers or {}
    local rows = elem.rows or {}

    local alignment_spec = ""
    for i, align in ipairs(aligns) do
      if align == "AlignLeft" then
        alignment_spec = alignment_spec .. "l"
      elseif align == "AlignRight" then
        alignment_spec = alignment_spec .. "r"
      elseif align == "AlignCenter" then
        alignment_spec = alignment_spec .. "c"
      else
        alignment_spec = alignment_spec .. "l"
      end
    end

    local caption_text = get_caption_text(caption)
    local table_latex = "\\begin{table}[h]\n\\centering\n"
    if caption_text ~= "" then
      table_latex = table_latex .. "\\caption{" .. caption_text .. "}\n"
    end
    table_latex = table_latex .. "\\begin{tabular}{" .. alignment_spec .. "}\n"
    table_latex = table_latex .. "\\toprule\n"
    
    local header_cells = {}
    for i, cell in ipairs(headers) do
      table.insert(header_cells, pandoc.utils.stringify(cell))
    end
    table_latex = table_latex .. table.concat(header_cells, " & ") .. " \\\\\n"
    table_latex = table_latex .. "\\midrule\n"
    
    for i, row in ipairs(rows) do
      local cell_texts = {}
      for j, cell in ipairs(row) do
        table.insert(cell_texts, pandoc.utils.stringify(cell))
      end
      table_latex = table_latex .. table.concat(cell_texts, " & ") .. " \\\\\n"
    end
    
    table_latex = table_latex .. "\\bottomrule\n"
    table_latex = table_latex .. "\\end{tabular}\n\\end{table}"
    
    return pandoc.RawBlock("latex", table_latex)
  
  -- Estructura nueva (Pandoc 2.11+)
  else
    local caption = elem.caption
    local colspecs = elem.colspecs or {}
    local head = elem.head or {}
    local bodies = elem.bodies or {}
    local foot = elem.foot or {}
    
    local alignment_spec = ""
    for i, cs in ipairs(colspecs) do
      local align = cs[2]
      if align == "AlignLeft" then
        alignment_spec = alignment_spec .. "l"
      elseif align == "AlignRight" then
        alignment_spec = alignment_spec .. "r"
      elseif align == "AlignCenter" then
        alignment_spec = alignment_spec .. "c"
      else
        alignment_spec = alignment_spec .. "l"
      end
    end

    local caption_text = get_caption_text(caption)
    local table_latex = "\\begin{table}[h]\n\\centering\n"
    if caption_text ~= "" then
      table_latex = table_latex .. "\\caption{" .. caption_text .. "}\n"
    end
    table_latex = table_latex .. "\\begin{tabular}{" .. alignment_spec .. "}\n"
    table_latex = table_latex .. "\\toprule\n"
    
    if head and head.rows and #head.rows > 0 then
      local header_row = head.rows[1]
      local header_cells = {}
      for i, cell in ipairs(header_row.cells) do
        table.insert(header_cells, pandoc.utils.stringify(cell))
      end
      table_latex = table_latex .. table.concat(header_cells, " & ") .. " \\\\\n"
      table_latex = table_latex .. "\\midrule\n"
    end
    
    if bodies and #bodies > 0 then
      for i, body in ipairs(bodies) do
        for j, row in ipairs(body.rows) do
          local cell_texts = {}
          for k, cell in ipairs(row.cells) do
            table.insert(cell_texts, pandoc.utils.stringify(cell))
          end
          table_latex = table_latex .. table.concat(cell_texts, " & ") .. " \\\\\n"
        end
      end
    end
    
    table_latex = table_latex .. "\\bottomrule\n"
    table_latex = table_latex .. "\\end{tabular}\n\\end{table}"
    
    return pandoc.RawBlock("latex", table_latex)
  end
end
