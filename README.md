# INFO
Stupid simple utility that uses the file_sigs_RAW.txt ( which you can find in the FileSig zip [HERE](https://www.garykessler.net/software/) ) to search in a binary file for all the file headers it hypothetically contains

# USAGE

Normal usage:
```main.py -f file.bin ```

Whit offset limit:
```main.py -f file.bin -o 0x1d85```

With offset limit and headed lenght limit
```main.py -f file.bin -o 0x1d85 -l 4```
