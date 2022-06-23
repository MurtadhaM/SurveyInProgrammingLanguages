/**
 * @author Murtadha Marzouq
 */

import React, { useState, useEffect } from "react";
import "../styles/globals.css";
import Layout from "../components/Layout";
import LoadingScreen from "../components/LoadingScreen";
import { ThemeProvider } from "../components/ThemeContext";

function App({ Component, pageProps }) {
	//State to hold if Staff and School JSONs are loaded

	/**
	 * A hook that sets the state to hold if Staff and School JSONs are loaded.
	 * @param {boolean} loaded - the state of the loaded state.
	 * @returns None
	 */
	const [loaded, setLoaded] = useState(false);

	/**
	 * Fetches the school and staff data from the API and stores it in localStorage.
	 * @returns None
	 */
	useEffect(() => {
		if (localStorage.getItem("staffWithScholar") == null) {
			//Fetch both files that are used in project
			Promise.all([
				fetch(
					"https://raw.githubusercontent.com/HullRyan/test_data/main/school_newest.json"
				),
				fetch(
					"https://raw.githubusercontent.com/HullRyan/test_data/main/StaffWithScholarData.json"
				),
			])
				//Convert to JSON
				.then((responses) => Promise.all(responses.map((r) => r.json())))
				.then(([school, staff]) => {
					console.log(school, staff);
					//Store objects in localStorage for use in components
					localStorage.setItem("school", JSON.stringify(school));
					localStorage.setItem("staffWithScholar", JSON.stringify(staff));
					setLoaded(true);
				});
		} else setLoaded(true);
	}, []);

	return (
		<ThemeProvider>
			{/* State updates will display loading screen if false, normal components and layout is true */}
			{loaded === true ? (
				<Layout>
					<Component {...pageProps} />
				</Layout>
			) : (
				<LoadingScreen />
			)}
		</ThemeProvider>
	);
}

export default App;
