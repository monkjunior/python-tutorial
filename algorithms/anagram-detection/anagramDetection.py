def checkOffAlgorithm(str1, str2):
    if ( type(str1) is str and type(str2) is str ):
        if (len(str1) != len(str2)):
            print("Different string's lengths")
            return False        
        # Check off algorithms
        # It looks like a BruteForce Alg
        i = 0
        for c1 in str1:
            for c2 in str2:
                if (c1 is c2):
                    str2 = str2.replace(c2, '', 1)
                    i = i + 1
        # Complexity: O[n*(n+1)/2]
        if (i == len(str1)):
            print("TRUE")
            return True
        else:
            print("FALSE")
            return False
    else:
        print("Wrong type")
        return False

def sortAndCompare(str1, str2):
    if ( type(str1) is str and type(str2) is str ):
        if (len(str1) != len(str2)):
            print("Different string's lengths")
            return False
        
        # Sort and Compare
        # After sort, you just need to loop n times
        # But we pay addition cost for 2 sort methods, may by O(n*n) or O(nlog(n))
        # So this algorithms has the same order of magnitude as that of sorting processes
        s1 = list(str1)
        s2 = list(str2)
        s1.sort()
        s2.sort()
        
        i = 0
        while (i < len(s1)):
            if (s1[0] is s2[0]):
                i = i + 1
            else:
                print("FALSE")
                return False 
        print("TRUE")
        return True
    else:
        print("Wrong type")
        return False

def countAndCompare(str1, str2):
    # Suppose strings just include 26 lower case alphabet charaters
    # 'a' --> 97  'z' --> 122
    c1 = [0]*26
    c2 = [0]*26
    for index in range(len(str1)):
        i = ord(str1[index]) - ord('a')
        c1[i] = c1[i] + 1

    for index in range(len(str2)):
        i = ord(str1[index]) - ord('a')
        c2[i] = c2[i] + 1

    for index in range(26):
        if (c1[index] != c2[index]):
            print("FALSE")
            return False
    print("TRUE")
    return True

