def remove_ensuremath(input_filename,output_filename="output.txt"):
    with open(input_filename,"r") as f:
        in_text = f.read()

    out_text = ""
    stack = []
    good_indices = []
    i = 0

    while i < len(in_text):
        if in_text[i:i+12] == r'\ensuremath{':
            good_indices.append(True)
            stack.append('')
            i += 12
        elif in_text[i] == '{':
            good_indices.append(False)
            stack.append('')
            i += 1
        elif in_text[i] == '}':
            if not stack:
                out_text += '}'
            elif len(stack) == 1:
                if good_indices.pop():
                    out_text += stack.pop()
                else:
                    out_text += '{' + stack.pop() + '}'
            else:
                new_text = stack.pop()
                if good_indices.pop():
                    stack[-1] += new_text
                else:
                    stack[-1] += '{' + new_text + '}'
            i += 1
        else:
            if stack:
                stack[-1] += in_text[i]
            else:
                out_text += in_text[i]
            i += 1

    with open(output_filename,"w") as f:
        f.write(out_text)

if __name__ == "__main__":
    remove_ensuremath("input.txt")