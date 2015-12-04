echo "============================================"
echo "||           Raptor Bechmarck             ||"
echo "============================================"
echo "================ 10 ==================="
echo "===   PyRaptor   ==="
time python ./src/raptor_v2.py -p ./lab/PyRaptor/10 -s 3 -a original -c sg

echo "=== PyRaptor old ==="
time python ./src/raptor_old.py -p ./lab/PyRaptor_old/10 -s 3 -a original -c sg

echo "=== Haskell old ==="
time raptor sg 3 original ./lab/Haskell/10

echo "================ 50 ==================="
echo "===   PyRaptor   ==="
time python ./src/raptor_v2.py -p ./lab/PyRaptor/50 -s 10 -a original -c sg

echo "=== PyRaptor old ==="
time python ./src/raptor_old.py -p ./lab/PyRaptor_old/50 -s 10 -a original -c sg

echo "=== Haskell old ==="
time raptor sg 3 original ./lab/Haskell/50

echo "================ 100 =================="
echo "===   PyRaptor   ==="
time python ./src/raptor_v2.py -p ./lab/PyRaptor/100 -s 30 -a original -c sg

echo "=== PyRaptor old ==="
time python ./src/raptor_old.py -p ./lab/PyRaptor_old/100 -s 30 -a original -c sg

echo "=== Haskell old ==="
time raptor sg 30 original ./lab/Haskell/100

echo "================ 500 =================="
echo "===   PyRaptor   ==="
time python ./src/raptor_v2.py -p ./lab/PyRaptor/500 -s 30 -a original -c sg

echo "=== PyRaptor old ==="
time python ./src/raptor_old.py -p ./lab/PyRaptor_old/500 -s 30 -a original -c sg

echo "=== Haskell old ==="
time raptor sg 30 original ./lab/Haskell/500

echo "================ 1000 ================="
echo "===   PyRaptor   ==="
time python ./src/raptor_v2.py -p ./lab/PyRaptor/1000 -s 30 -a original -c sg

echo "=== PyRaptor old ==="
time python ./src/raptor_old.py -p ./lab/PyRaptor_old/1000 -s 30 -a original -c sg

echo "=== Haskell old ==="
time raptor sg 30 original ./lab/Haskell/1000

echo "================ 5000 ================="
echo "===   PyRaptor   ==="
time python ./src/raptor_v2.py -p ./lab/PyRaptor/5000 -s 30 -a original -c sg

echo "=== PyRaptor old ==="
time python ./src/raptor_old.py -p ./lab/PyRaptor_old/5000 -s 30 -a original -c sg

echo "=== Haskell old ==="
time raptor sg 30 original ./lab/Haskell/5000

echo "================ 10000 ================"
echo "===   PyRaptor   ==="
time python ./src/raptor_v2.py -p ./lab/PyRaptor/10000 -s 30 -a original -c sg

echo "=== PyRaptor old ==="
time python ./src/raptor_old.py -p ./lab/PyRaptor_old/10000 -s 30 -a original -c sg

echo "=== Haskell old ==="
time raptor sg 30 original ./lab/Haskell/10000