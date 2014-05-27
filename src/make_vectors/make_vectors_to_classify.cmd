input_file = /workspace/ling575_2014/abothale-riamarie/data/train.pickle
output_file = /workspace/ling575_2014/abothale-riamarie/data/mallet/train.vectors.to_classify.txt

Executable = make_vectors_to_classify.sh
arguments = $(input_file) $(output_file)
Universe   = vanilla
getenv     = true
output     = tmp/out.out
error      = tmp/err.err
Log        = tmp/log.log
transfer_executable = false
request_memory = 1024
Queue

input_file = /workspace/ling575_2014/abothale-riamarie/data/test.pickle
output_file = /workspace/ling575_2014/abothale-riamarie/data/mallet/test.vectors.to_classify.txt
Queue