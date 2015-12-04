echo "============================================"
echo "||      Optimized PyRaptor Bechmark       ||"
echo "============================================"
echo "================ 10 ==================="
time pypy ./src/raptor_v2.py -p ./lab/PyRaptor/10 -s 3 -a original -c sg

echo "================ 50 ==================="
time pypy ./src/raptor_v2.py -p ./lab/PyRaptor/50 -s 10 -a original -c sg

echo "================ 100 =================="
time pypy ./src/raptor_v2.py -p ./lab/PyRaptor/100 -s 30 -a original -c sg

echo "================ 500 =================="
time pypy ./src/raptor_v2.py -p ./lab/PyRaptor/500 -s 30 -a original -c sg

echo "================ 1000 ================="
time pypy ./src/raptor_v2.py -p ./lab/PyRaptor/1000 -s 30 -a original -c sg

echo "================ 5000 ================="
time pypy ./src/raptor_v2.py -p ./lab/PyRaptor/5000 -s 30 -a original -c sg

echo "================ 10000 ================"
time pypy ./src/raptor_v2.py -p ./lab/PyRaptor/10000 -s 30 -a original -c sg