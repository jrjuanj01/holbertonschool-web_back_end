export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  set name(value) {
    this._name = value;
  }

  get name() {
    return this._name;
  }

  set students(value) {
    this._students = value;
  }

  get students() {
    return this._students;
  }

  set length(value) {
    this._length = value;
  }

  get length() {
    return this._length;
  }
}
