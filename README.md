# toolbelt

A collection of quick command line tools.

## Install:
The installation script places symlinks inside `/usr/local/bin`.
```
git clone https://github.com/shanereilly/toolbelt
cd ./toolbelt
sudo ./install.sh
```

## Uninstall:
```
sudo ./uninstall.sh
```

## Tools
- **bcd** convert decimal, hexidecimal or octal number to BCD or convert BCD to decimal `bcd [-b | -d | -x | -o] number`
- **bin2dec** convert binary number to decimal `bin2dec [--signed --wordsize size] infile`
- **bitcmp** compares two files, bit by bit `bitcmp file1 file2 [count]`
- **dec2bin** convert decimal number to binary `dec2bin [--pad --wordsize size] infile`
- **install.sh** install script
- **uninstall.sh** uninstall script
- **xor** XOR encoder/decoder `xor file1 file2` 

