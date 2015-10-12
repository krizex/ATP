#!/bin/bash

ROOT_DIR="`pwd`/.."
CAPTURE_SCRIPT="${ROOT_DIR}/casperjs/qunar.js"
ANALYSIS_SCRIPT="${ROOT_DIR}/atp/main.py"

LOGFILE="${ROOT_DIR}/launch/run.log"
function log
{
	curTime=`date "+%Y-%m-%d %H:%M:%S"`
	echo "${curTime} $*" >> ${LOGFILE}
}

function main
{
	i=0
	while [ $i -lt 45 ];do
		i=`expr $i + 1`
		searchDate=`date --date="$i day" "+%Y-%m-%d"`
		retryTime=0
		ok=0
		while [ ${retryTime} -lt 5 ];do
			retryTime=`expr ${retryTime} + 1`
			casperjs ${CAPTURE_SCRIPT} ${searchDate}
		    if [ $? -ne 0 ];then
		        log "[${retryTime}] search by day[${searchDate}] failed"
		        continue
		    fi
		    
		    ok=1
		    break
		done
		
		if [ ${ok} -ne 1 ];then
			log "search for date[${searchDate}] failed."
			continue
		fi
	
	    python ${ANALYSIS_SCRIPT} "searchResult.html" "${searchDate}"
	    log "search date[${searchDate}] succeed."
	done
}

log "Begin collect..."
main
log "End collect..."
