def permutations(s):
    if len(s) == 1:
        return [s]  
    perms = []  
    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i+1:]  
        for p in permutations(remaining):  
            perms.append(char + p)  
    return perms

# Example Usage
input_string = "abc"
all_permutations = permutations(input_string)
print(f"All permutations of '{input_string}': {all_permutations}")
