#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = 1
    print((len(sys.argv) - 1),"arguments:")
    for i in sys.argv:
        if i != sys.argv[0]:


            print(a, ":", i)
            a = a + 1
