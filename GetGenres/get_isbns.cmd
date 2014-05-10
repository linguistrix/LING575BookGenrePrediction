input_dir = /workspace/ling575_2014/abothale-riamarie/filtered_reviews_isbn/
output_file = isbn_list.txt

Executable = get_isbns.sh
arguments =  $(input_dir) $(output_file)
Universe   = vanilla
getenv     = true
output     = out.out
error      = err.err
Log        = log.log
transfer_executable = false
request_memory = 1024
Queue