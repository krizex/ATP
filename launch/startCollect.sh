#!/bin/bash

ROOT_DIR="`pwd`/.."
CAPTURE_SCRIPT="${ROOT_DIR}/casperjs/qunar.js"
ANALYSIS_SCRIPT="${ROOT_DIR}/atp/main.py"


function main
{
    curDate=`date --date='+1 day' "+%Y-%m-%d"`
    casperjs ${CAPTURE_SCRIPT} ${curDate}
    if [ $? -ne 0 ];then
        echo "search by day[${curDate}] failed"
        return 1
    fi

    python ${ANALYSIS_SCRIPT} "searchResult.html"
}

main
