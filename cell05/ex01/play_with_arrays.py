#!/usr/bin/env python3

def main():
    
    OriginalArray = [2, 8, 9, 48, 8, 22, -12, 2]
    NewArry = [x + 2 for x in OriginalArray]
    
    print(f"Original array: {OriginalArray}")
    print(f"New array: {NewArry}")

main()