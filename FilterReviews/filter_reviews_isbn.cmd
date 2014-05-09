input_dir = /workspace/ling575_2014/abothale-riamarie/filtered_reviews/
output_dir = /workspace/ling575_2014/abothale-riamarie/filtered_reviews_isbn/

Executable = filter_reviews_isbn.sh
arguments =  $(input_dir) $(output_dir)
Universe   = vanilla
getenv     = true
output     = out.out
error      = err.err
Log        = log.log
transfer_executable = false
request_memory = 1024
Queue