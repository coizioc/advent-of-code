scriptFile=./py/year$1/day$2.py

if [ ! -e $scriptFile ]; then
    >&2 echo "${scriptFile} does not exist!"
    exit 1
fi


timeout 60s python $scriptFile || {
    exit_status=$?
    if [[ $exitStatus -eq 125 ]]; then
        >&2 echo "Script timed out!"
    fi
    exit 1
}

exit 0