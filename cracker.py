alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
secret = "cat4"
found = False
attempts = 0

for c1 in alphabet:
    for c2 in alphabet:
        for c3 in alphabet:
            for c4 in alphabet:
                attempt = c1 + c2 + c3 + c4
                attempts += 1
                if attempt == secret:
                    found = True
                    print("Password found:", attempt)
                    print("Attempts:", attempts)
                    break

            if found:
                break
        if found:
            break
    if found:
        break