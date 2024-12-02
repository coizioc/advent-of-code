success="true"

scriptFile=com/aoc/year$1/Day$2.java

if [ ! -e "$scriptFile" ]; then
    >&2 echo "${scriptFile} does not exist!"
    exit 1
fi

javac $scriptFile
java com.aoc.year$1.Day$2 || {
    success="false"
}

if [ $success = "false" ]; then
    exit 1;
fi

exit 0