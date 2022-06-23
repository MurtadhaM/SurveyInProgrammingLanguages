/**
  * @author Murtadha Marzouq

 */

import React, { useState, useEffect, useContext } from "react";

/**
 * A React context that holds the current theme.       
 * @type {React.Context<string>}       
 */
const ThemeContext = React.createContext("light");

/**
 * The ThemeProvider component is used to provide the theme to the rest of the application.
 * @param {React.ReactNode} children - The children of the component.
 * @returns None
 */
export function ThemeProvider({ children }) {

	/**
	 * A hook that sets the theme of the page.
	 * @returns None
	 */
	const [theme, setTheme] = useState(global.window?.__theme || "light");
	
	/**
	 * Toggles the theme of the page between light and dark modes.
	 * @returns None
	 */
	const toggleTheme = () => {
		global.window.__setPreferredTheme(theme === "light" ? "dark" : "light");
	};

	/**
	 * Sets the theme of the page.
	 * @param {string} theme - the theme to set the page to.
	 * @returns None
	 */
	useEffect(() => {
		global.window.__onThemeChange = setTheme;
	}, []);

	return (
		<ThemeContext.Provider value={{ theme, toggleTheme }}>
			{children}
		</ThemeContext.Provider>
	);
}

export const useTheme = () => useContext(ThemeContext);
export default ThemeContext;
