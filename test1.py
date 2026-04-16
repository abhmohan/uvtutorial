import test

''' 
Running the greet function from test.py automatically because I didn't use
if __name__ == "__main__":

This breaks modular design.

❌ When ignoring it causes problems
1️⃣ Code runs unintentionally when imported

Without it:

def main():
    print("Hello")

main()   # always runs!


Then:

import myfile   # 😱 main() runs automatically


This breaks modular design.

2️⃣ Breaks unit testing

Test files importing your module will trigger execution:

import myfile   # main() runs unexpectedly


Causing:

side effects

DB connections opening

servers starting

prints/logs appearing

3️⃣ Bad for FastAPI, Flask, servers

Example:

app = FastAPI()

uvicorn.run(app)


If imported → server starts automatically ❌
Correct pattern:

if __name__ == "__main__":
    uvicorn.run(app)


Without this:

Tests fail

Importing app in other files breaks

4️⃣ Circular import issues

If files import each other and code runs at import time → 💥 crashes or weird bugs.

Best practice (recommended for you)

Since you’re working with:

FastAPI

backend scripts

reusable modules

👉 You should always use it when writing executable logic.
'''