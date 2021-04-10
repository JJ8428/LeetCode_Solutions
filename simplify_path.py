class Solution:
    def simplifyPath(self, path: str) -> str:
        
        canon = []
        while path.__contains__("//"):
            path = path.replace("//", "/")
        try:
            if path[0] == "/":
                path = path[1:]
            if path[-1] == "/":
                path = path[:-1]
        except:
            pass
        path = path.split("/")
        for dirs in path:
            if dirs == "..":
                try:
                    canon.pop(-1)
                except:
                    continue
            elif dirs != ".":
                canon.append(dirs)
        canon_path = "/"
        for val in canon:
            canon_path += val + "/"
        if canon_path != "/":
            canon_path = canon_path[:-1]
        return canon_path