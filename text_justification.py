class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        output = []
        current_line = ""
        line_words = []
        while words.__len__() != 0:
            curr = ""
            total_length = 0
            non_spaces = 0
            last_index = 0
            for a in range(0, words.__len__()):
                total_length += (words[a].__len__() + 1)
                if total_length-1 <= maxWidth:
                    line_words.append(words[a])
                    non_spaces += words[a].__len__()
                    last_index = a
                else:
                    break
            words = words[last_index+1:]
            for a in range(1, (line_words.__len__()*2)-1, 2):
                line_words.insert(a, "")
            print(line_words)
            to_add = maxWidth - non_spaces
            indices = [i for i, x in enumerate(line_words) if x == ""]
            if indices.__len__() == 0:
                indices = [0]
            _indices = 0
            while to_add != 0:
                to_add -= 1
                line_words[indices[_indices]] += " "
                _indices += 1
                if _indices == indices.__len__():
                    _indices = 0
            output.append("".join(line_words))
            line_words = []
        last_line = output.pop(-1)
        while last_line.__contains__("  "):
            last_line = last_line.replace("  ", " ")        
        if last_line[-1] == " ":
            last_line = last_line[:-1]
        to_add = maxWidth - last_line.__len__()
        for a in range(0, to_add):
            last_line += " "
        output.append(last_line)
        return output
            