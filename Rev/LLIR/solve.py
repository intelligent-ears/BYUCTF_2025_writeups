def solve_flag():
    flag = [None] * 37
    flag[0:6] = list("byuctf") 
    flag[6] = '{'            
    flag[36] = '}'               
    t_val = flag[4] = flag[14] = flag[17] = flag[23] = flag[25] = 't'
    flag[31] = '_'
    flag[9] = flag[20] = '1'
    flag[8] = chr(ord(flag[9]) + 27) 
    flag[7] = chr(ord(flag[8]) + 32)  
    flag[10] = chr(ord(flag[7]) + 6) 
    flag[18] = flag[10] 
    flag[11] = flag[15] = flag[24] = flag[27] = flag[31]  
    flag[13] = chr(ord(flag[10]) - 3) 
    flag[26] = flag[13]  
    flag[12] = chr(ord(flag[13]) - 1)  
    flag[16] = chr(ord(flag[14]) - 1) 
    flag[29] = flag[16] 
    flag[21] = chr(ord(flag[5]) + 1) 
    flag[22] = chr(ord(flag[21]) + 1) 
    flag[28] = chr(ord(flag[22]) // 2) 
    flag[19] = flag[28] 
    flag[32] = flag[28]
    flag[35] = chr(ord(flag[5]) - 2)
    flag[33] = chr(ord(flag[32]) + 1) 
    flag[34] = chr(ord(flag[33]) + 3)  
    flag[30] = chr(ord(flag[7]) + 1) 
    verify_flag(flag)

    return ''.join(flag)

def verify_flag(flag):
    f = [ord(c) if c is not None else 0 for c in flag]
    
    # Check all constraints
    assert f[4] == f[14] == f[17] == f[23] == f[25] == ord('t')
    assert f[9] == f[20] == ord('1')
    assert f[10] == f[18] == ord('r')
    assert f[11] == f[15] == f[24] == f[31] == f[27] == ord('_')
    assert f[13] == f[26] == ord('o')
    assert f[12] == f[13] - 1 == ord('n')
    assert f[16] == f[29] == ord('s')
    assert f[19] == f[28] == f[32] == ord('4')
    assert f[21] == ord('g')
    assert f[22] == ord('h')
    assert f[35] == ord('d')
    assert f[33] == ord('5')
    assert f[34] == ord('8')
    assert f[30] == ord('m')
    assert f[8] == f[7] - 32
    assert f[9] + f[20] == f[31] + 3 == ord('b')
    assert f[10] == f[7] + 6
    assert f[8] == f[9] + 27
    assert f[5] == f[21] - 1
    assert f[21] == f[22] - 1
    assert f[22] == f[28] * 2
    assert f[33] == f[32] + 1
    assert f[32] + 1 == f[34] - 3
    assert f[30] == f[7] + 1
    print("All constraints verified successfully!")

if __name__ == "__main__":
    flag = solve_flag()
    print(f"Solved flag: {flag}")
