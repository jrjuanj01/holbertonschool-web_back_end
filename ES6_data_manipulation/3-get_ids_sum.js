export default function getStudentIdsSum(list) {
  const initial = 0;
  const sum = list.reduce((acc, curr) => acc + curr, initial);
  return sum;
}
