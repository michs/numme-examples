#!/usr/bin/python

if not 'write_pycode' in vars():
    from pygments import highlight
    from pygments.lexers import PythonLexer
    from pygments.formatters import HtmlFormatter
    import IPython

    def write_pycode(fname):
        with open('newton.py') as f:
            code = f.read()

        formatter = HtmlFormatter()
        return IPython.display.HTML('<style type="text/css">{}</style>{}'.format(
            formatter.get_style_defs('.highlight'),
            highlight(code, PythonLexer(), formatter)))
