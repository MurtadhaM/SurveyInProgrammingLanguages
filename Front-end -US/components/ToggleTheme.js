/**
  * @author Murtadha Marzouq

 */

import React, { useState, useEffect } from "react";
import { BiMoon, BiSun } from "react-icons/bi";
import { useTheme } from "./ThemeContext";

/**
 * A button that toggles the theme of the page.
 * @returns None
 */
function ToggleTheme() {
	
	/**
	 * A hook that sets the mount state to true when the component is mounted.
	 * @returns None
	 */
	const [mount, setMount] = useState(false);
	/**
	 * A custom hook that returns the current theme and a function that toggles the theme.
	 * @returns {[Theme, () => void]} - The current theme and a function that toggles the theme.
	 */
	const { theme, toggleTheme } = useTheme();

	/**
	 * A React hook that sets the mount state to true.
	 * @returns None
	 */
	useEffect(() => {
		setMount(true);
	}, []);

	if (!mount) return null;

	return (
		<button type="button" onClick={toggleTheme} className={theme}>
			{theme === "light" ? <BiMoon /> : <BiSun />}
			<style jsx>{`
				button {
					/* remove default */
					background: none;
					color: inherit;
					border: none;
					padding: 0;
					font: inherit;
					cursor: pointer;
					outline: inherit;
					/* custom styles */
					display: flex;
					justify-content: center;
					align-items: center;
					font-size: 1.4rem;
					padding: 4px;
					border-radius: 2px;
				}
				.light {
					color: #2d3748;
				}
				.dark {
					color: #f6e05e;
				}
			`}</style>
		</button>
	);
}

export default ToggleTheme;
