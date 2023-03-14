import json

class VizText (gdb.Function):
  """Visualize multiline Text in an editor.
Takes a text as an argument. You can provide a file name
as a second argument to enable highlighting.
If you provide another text as a third argument, then
it will show you a diff.
set print elements unlimited
--language minimal $vizText(Text)"""

  def __init__ (self):
    super (VizText, self).__init__ ("vizText")

  def invoke (self, text, fileName=None, otherText=None):
    val = {"kind": {"text": True}, "text": text.string()}
    if fileName:
        val["fileName"] = fileName.string()
    if otherText:
        val["otherText"] = otherText.string()
    return json.dumps(val)













class VizGrid (gdb.Function):
  """Visualize a data as a Grid.
Takes a Grid as an argument."""

  def __init__ (self):
    super (VizGrid, self).__init__ ("vizGrid")

  def invoke (self, data):
    dat = data
    typ = dat.type
    val = {"kind": {"grid": True}, "rows": [{"columns":[]}]}
    if typ.code == gdb.TYPE_CODE_ARRAY:
        first_index, last_index = typ.range()
        for i in range(first_index, last_index + 1):
            item = dat[i]
            val["rows"][0]["columns"].append({"content": str(item), "tag": str(i)})

    return json.dumps(val)


class VizPlot (gdb.Function):
  """Visualize a data as a Plot.
Takes a Plot as an argument."""

  def __init__ (self):
    super (VizPlot, self).__init__ ("vizPlot")

  def invoke (self, data):
    dat = data
    typ = dat.type
    val = {"kind": {"plotly": True}, "data": [{"y":[]}]}
    if typ.code == gdb.TYPE_CODE_ARRAY:
        first_index, last_index = typ.range()
        for i in range(first_index, last_index + 1):
            item = dat[i]
            val["data"][0]["y"].append(int(item))

    return json.dumps(val)

VizText ()
VizGrid ()
VizPlot ()
