import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";

const Menu = ({data}) =>
    !data.length ? (
        <p>Nothing to show</p>
    ) : (
        // code for menu here
        <div></div>
    );
Menu.propTypes = {
    data: PropTypes.array.isRequired
};
export default Menu;