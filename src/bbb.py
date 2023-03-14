class VizCall (gdb.Function):
  def __init__ (self):
    super (VizCall, self).__init__ ("vizCall")
  def invoke (self, name, arg):
    """ This will find a global function with given name
        and call it with given argument (arg). The function
        should return String. The result will be converted
        to plain Python string with escape characters stripped.
    """
    text=name.string()
    sym = gdb.lookup_global_symbol(text)
    funct = sym.value()
    val = funct(arg)['P_ARRAY'].dereference ()
    val = val.format_string(pretty_arrays=False,symbols=False,address=False)
    val = val.encode('raw_unicode_escape').decode('unicode_escape')
    val = val[1:-1]
    #val = eval(val)
    return val

VizCall ()
