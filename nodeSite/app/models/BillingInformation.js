/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('BillingInformation', {
    BillingInformationID: {
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true,
      autoIncrement: true
    },
    CreditCardNumber: {
      type: DataTypes.INTEGER(11),
      allowNull: true
    },
    ExpirationDate: {
      type: DataTypes.DATEONLY,
      allowNull: true
    },
    AddressID: {
      type: DataTypes.BIGINT,
      allowNull: true,
      references: {
        model: 'Address',
        key: 'AddressID'
      }
    }
  }, {
    tableName: 'BillingInformation'
  });
};
