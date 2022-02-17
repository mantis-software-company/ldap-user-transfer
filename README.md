
# ldap-user-transfer

Script for transferring LDAP users from Postgresql database. Tested only in OpenLDAP, may work in others.

## Configuration

- db : 
	- user_sql: Sql query for fetching users. (Cast id column to varchar) 
	- group_sql: Sql query for getting group of user (Cast id column to varchar)
	- user_pk: Id column of user table
	- user_password_column: Password column of user in plain text. If this property given, userPassword field on LDAP will filled password with SHA-512 encryption in CRYPT format. 
	- group_pk: Id column of group table
	- cursor_fetch_size: This script use postgresql binary cursors to iterate large amount of user rows. You can set cursor fetch size with this value.

- ldap: 
	- user_base: user base DN without base DN
	- group_base:  group base DN without base DN
	- user_classes: LDAP classes of user object (as list)

-  mappings:
	- user_fields: mapping of user table column names  and LDAP attributes in <String, String> or <String, List> formats.
	- groups: mapping of group names on db and LDAP group names in <String, String> format. Use id column of groups table for mapping.

## Usage

After installing package from PyPI, define your config.yml path via `LDAP_USER_TRANSFER_CONFIG` environment variable then run `ldap-transfer-user` command.