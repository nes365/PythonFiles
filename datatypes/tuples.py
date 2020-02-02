

def main():
    tup1=(1,2,3)
    tup2=(4,5,6)
    tup3=tup1+tup2
    print_tup(tup3)
    
def print_tup(o):
    for i in o:
            print(i, end=' ', flush=True)
            print()
                
    
if __name__ == '__main__': main()