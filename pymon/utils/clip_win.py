import ctypes


str_cpy = ctypes.cdll.msvcrt.strcpy
open_clipboard = ctypes.windll.user32.OpenClipboard
empty_clipboard = ctypes.windll.user32.EmptyClipboard
get_clipboard = ctypes.windll.user32.GetClipboardData
set_clipboard = ctypes.windll.user32.SetClipboardData
close_clipboard = ctypes.windll.user32.CloseClipboard
global_alloc = ctypes.windll.kernel32.GlobalAlloc
global_lock = ctypes.windll.kernel32.GlobalLock
global_unlock = ctypes.windll.kernel32.GlobalUnlock

GMEM_DDESHARE = 0x2000
CF_TEXT = 1


def paste(data):
    open_clipboard(None)

    empty_clipboard()

    allocated = global_alloc(GMEM_DDESHARE, len(bytes(data, "ascii")) + 1)

    kernel_lock = global_lock(allocated)

    str_cpy(ctypes.c_char_p(kernel_lock), bytes(data, "ascii"))

    global_unlock(allocated)

    set_clipboard(CF_TEXT, allocated)

    close_clipboard()


def copy():
    open_clipboard(None)

    contents = get_clipboard(CF_TEXT)

    data = ctypes.c_char_p(contents).value

    # gul(pcontents)

    close_clipboard()

    return data
