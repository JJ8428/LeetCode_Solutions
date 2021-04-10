class Solution:
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        p_ip = []
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    for d in range(1, 4):
                        if a + b + c + d == s.__len__():
                            ip1 = s[0:a]
                            ip2 = s[a:a+b]
                            ip3 = s[a+b:a+b+c]
                            ip4 = s[a+b+c:a+b+c+d]
                            if int(ip1) <= 255 and \
                               int(ip2) <= 255 and \
                               int(ip3) <= 255 and \
                               int(ip4) <= 255:
                                if (ip1.__len__() > 1 and ip1[0] == "0") or \
                                   (ip2.__len__() > 1 and ip2[0] == "0") or \
                                   (ip3.__len__() > 1 and ip3[0] == "0") or \
                                   (ip4.__len__() > 1 and ip4[0] == "0"):
                                    continue
                                else:
                                    p_ip.append(ip1 + "." + ip2 + "." + ip3 + "." + ip4)
                            
        return p_ip