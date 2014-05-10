isbn_list_file = /workspace/ling575_2014/abothale-riamarie/GetGenres/isbn_list.txt
genre_output_file = genres.txt

Executable = get_genres.sh
arguments = $(isbn_list_file) $(genre_output_file)
Universe   = vanilla
getenv     = true
output     = out.out
error      = err.err
Log        = log.log
transfer_executable = false
request_memory = 1024
Queues