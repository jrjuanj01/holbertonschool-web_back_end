export default class Building {
  /**
     * @param {Number} sqft
     */
  constructor(sqft) {
    this._sqft = sqft;
    if (new.target === Building) {
      throw new Error('Cannot instantiate abstract class Building directly');
    }
  }

  get sqft() {
    return this._sqft;
  }

  /* eslint-disable */
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
  /* eslint-enable */
}
