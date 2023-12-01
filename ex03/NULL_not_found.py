import inspect
import re

def NULL_not_found(object: any):
    frame = inspect.currentframe()
    try:
        context = inspect.getframeinfo(frame.f_back).code_context
        caller_lines = ''.join([line.strip() for line in context])
        m = re.search(r'echo\s*\((.+?)\)$', caller_lines)
        if m:
            caller_lines = m.group(1)
    finally:
        del frame
    print(caller_lines)


    # print(type(object))