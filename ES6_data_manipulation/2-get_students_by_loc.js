export default function getStudentByLocation(list, city) {
  return list.filter((std) => std.location === city);
}