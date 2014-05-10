isbn_list_file = /workspace/ling575_2014/abothale-riamarie/GetGenres/isbn_list.test.txt
genre_output_file = genres.txt

Executable = get_genres.sh
arguments = $(isbn_list_file) $(genre_output_file)
Universe   = vanilla
getenv     = true
output     = tmp/out.out
error      = tmp/err.err
Log        = tmp/log.log
transfer_executable = false
request_memory = 1024
Queues