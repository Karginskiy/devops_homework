#!/bin/bash

filename="availability_check-$(date +"%FT%H%M%S")"
log_filename="$filename.log"
error_filename="$filename.error"
exec &>> $filename

function check_availability() {
        declare -i counter
        counter=1
        url="$1:$2"
        echo --------- Checking the availability of $url ---------
        while [ $counter -ne 6 ]
        do
                curl $url 1>/dev/null 2>/dev/null
                if (($? != 0))
                then
                        echo ==== [$url] - Attempt $counter - UNAVAILABLE
                        echo $1 1>> $error_filename
                        return
                else
                        echo ==== [$url] - Attempt $counter - AVAILABLE
                fi
        counter+=1
        done
}

check_availability 192.168.0.1 80
check_availability 173.194.222.113 80
check_availability 87.250.250.242 80
