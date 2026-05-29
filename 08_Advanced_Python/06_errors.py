
while True:

    try: 
        a = int(input("Enter a number 1: "))
        b = int(input("Enter a number 2: "))

        print(f"The sum is: {a + b}")
    except:
        print("Some error occured! ")

print("-------")

while True:
    c = int(input("Enter a number 1: "))
    d = int(input("Enter a number 2: "))

    if d == 0:
        raise ValueError("Value do not divide by 0")
    print(f"The division is: {c/d}")






# ============================================================
#           PYTHON BUILT-IN EXCEPTIONS - COMPLETE LIST
# ============================================================

# ── 1. BASE CLASSES ─────────────────────────────────────────
try:
    pass
except BaseException:        # Root of ALL exceptions
    pass

try:
    pass
except Exception:            # Base for all normal exceptions
    pass


# ── 2. ARITHMETIC ERRORS ────────────────────────────────────
try:
    x = 1 / 0
except ZeroDivisionError:    # Division or modulo by zero
    pass

try:
    x = 10 ** 10 ** 10
except OverflowError:        # Result too large to represent
    pass

try:
    pass
except FloatingPointError:   # Floating point operation failed
    pass

try:
    pass
except ArithmeticError:      # Base class for all arithmetic errors
    pass


# ── 3. TYPE & VALUE ERRORS ──────────────────────────────────
try:
    x = "a" + 1
except TypeError:            # Wrong type passed to operation
    pass

try:
    x = int("abc")
except ValueError:           # Right type but wrong value
    pass

try:
    pass
except UnicodeError:         # Base class for Unicode errors
    pass

try:
    b"\x80".decode("utf-8")
except UnicodeDecodeError:   # Unicode decoding failed
    pass

try:
    "café".encode("ascii")
except UnicodeEncodeError:   # Unicode encoding failed
    pass

try:
    pass
except UnicodeTranslateError: # Unicode translation failed
    pass


# ── 4. LOOKUP ERRORS ────────────────────────────────────────
try:
    d = {}
    x = d["key"]
except KeyError:             # Dictionary key not found
    pass

try:
    lst = [1, 2]
    x = lst[5]
except IndexError:           # List index out of range
    pass

try:
    pass
except LookupError:          # Base class for KeyError & IndexError
    pass


# ── 5. NAME & ATTRIBUTE ERRORS ──────────────────────────────
try:
    print(undefined_var)
except NameError:            # Variable not defined
    pass

try:
    def fn():
        print(x)
        x = 5
    fn()
except UnboundLocalError:    # Local var used before assignment
    pass

try:
    x = 5
    x.hello()
except AttributeError:       # Object has no such attribute
    pass


# ── 6. FILE & OS ERRORS ─────────────────────────────────────
try:
    open("nofile.txt")
except FileNotFoundError:    # File does not exist
    pass

try:
    pass
except FileExistsError:      # File already exists
    pass

try:
    pass
except PermissionError:      # No permission for operation
    pass

try:
    pass
except IsADirectoryError:    # Expected file, got directory
    pass

try:
    pass
except NotADirectoryError:   # Expected directory, got file
    pass

try:
    pass
except TimeoutError:         # Operation timed out
    pass

try:
    pass
except BlockingIOError:      # Operation would block
    pass

try:
    pass
except InterruptedError:     # System call interrupted
    pass

try:
    pass
except OSError:              # Base class for all OS errors
    pass

try:
    pass
except IOError:              # Alias for OSError
    pass


# ── 7. CONNECTION ERRORS ────────────────────────────────────
try:
    pass
except ConnectionError:      # Base class for connection errors
    pass

try:
    pass
except ConnectionRefusedError:  # Connection refused
    pass

try:
    pass
except ConnectionResetError:    # Connection reset
    pass

try:
    pass
except ConnectionAbortedError:  # Connection aborted
    pass

try:
    pass
except BrokenPipeError:      # Pipe closed or broken
    pass


# ── 8. IMPORT ERRORS ────────────────────────────────────────
try:
    import blahblah
except ModuleNotFoundError:  # Module not found (specific)
    pass

try:
    pass
except ImportError:          # Base class for import errors
    pass


# ── 9. RUNTIME ERRORS ───────────────────────────────────────
try:
    pass
except RuntimeError:         # Generic runtime error
    pass

try:
    def fn(): return fn()
    fn()
except RecursionError:       # Max recursion depth exceeded
    pass

try:
    pass
except NotImplementedError:  # Abstract method not implemented
    pass

try:
    x = iter([])
    next(x)
    next(x)
except StopIteration:        # No more items in iterator
    pass

try:
    pass
except StopAsyncIteration:   # No more items in async iterator
    pass


# ── 10. MEMORY & SYSTEM ERRORS ──────────────────────────────
try:
    pass
except MemoryError:          # Out of memory
    pass

try:
    pass
except SystemError:          # Internal Python interpreter error
    pass

try:
    pass
except ReferenceError:       # Weak reference to deleted object
    pass

try:
    pass
except BufferError:          # Buffer operation failed
    pass


# ── 11. SYNTAX & INDENTATION ERRORS ────────────────────────
try:
    eval("def 123abc():")
except SyntaxError:          # Invalid Python syntax
    pass

try:
    pass
except IndentationError:     # Wrong indentation
    pass

try:
    pass
except TabError:             # Mixed tabs and spaces
    pass


# ── 12. SYSTEM & KEYBOARD ───────────────────────────────────
try:
    import sys
    sys.exit()
except SystemExit:           # sys.exit() was called
    pass

try:
    pass
except KeyboardInterrupt:    # User pressed Ctrl+C
    pass

try:
    pass
except GeneratorExit:        # Generator was closed
    pass


# ============================================================
#              CATCH-ALL TEMPLATE (Best Practice)
# ============================================================
try:
    pass  # your code here

except ZeroDivisionError:
    pass  # handle specific error first

except (TypeError, ValueError) as e:
    pass  # group similar errors

except Exception as e:
    pass  # catch all normal exceptions

except BaseException as e:
    pass  # catches EVERYTHING including Ctrl+C, sys.exit()

else:
    pass  # runs if NO exception occurred

finally:
    pass  # ALWAYS runs no matter what

















