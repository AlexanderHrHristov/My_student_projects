password = "123456"
counter = 0
is_found = False

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        counter += 1
                        combination = f"{i}{j}{k}{l}{m}{n}"
                        if combination == password:
                            is_found = True
                            break

                if is_found:
                    break
            if is_found:
                break
        if is_found:
            break
    if is_found:
        break

print(f"Number of iterations: {counter}")
