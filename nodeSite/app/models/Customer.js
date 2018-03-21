/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('Customer', {
    CustomerID: {
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true,
      autoIncrement: true
    },
    Email: {
      type: DataTypes.STRING(255),
      allowNull: true
    },
    cName: {
      type: DataTypes.STRING(255),
      allowNull: true
    },
    Pass: {
      type: DataTypes.STRING(255),
      allowNull: true
    },
    AddressID: {
      type: DataTypes.BIGINT,
      allowNull: true,
      references: {
        model: 'Address',
        key: 'AddressID'
      }
    },
    BillingInformationID: {
      type: DataTypes.BIGINT,
      allowNull: true,
      references: {
        model: 'BillingInformation',
        key: 'BillingInformationID'
      }
    }
  }, {
    tableName: 'Customer'
  });
};
