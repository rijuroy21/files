import React from "react";

class UserList extends React.Component {
    render() {
        return (
            <div>
                {this.props.users.length > 0 ? (
                    <ul>
                        {this.props.users.map((user) => (
                            <li key={user.id}>
                                <strong>Name : {user.name}</strong> email : {user.email} <br />
                                phone : {user.phone} <br />
                                Age : {user.age} <br />
                                occupation : {user.occupation} <br />
                                address : {user.address}
                            </li>
                        ))}
                    </ul>
                ) : (
                    <p>Loading users...</p>
                )}
            </div>
        );
    }
}

export default UserList;
