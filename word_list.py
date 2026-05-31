words = ["hello", "password", "trevor", "cat4", "secret", "test", "python"]
secret = "cat4"
found = False
attempts = 0

for attempt in words:
    attempts += 1
    if attempt == secret:
        found = True
        print("Password found:", attempt)
        print("Attempts:", attempts)
        break

if not found:
    print("Password not found in the dictionary.")
    
    #uses word list 