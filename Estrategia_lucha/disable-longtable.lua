function Table(el)
  el.attr = el.attr or pandoc.Attr()
  el.attr.classes = {"table"}
  return el
end
