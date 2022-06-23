/**
  * @author Murtadha Marzouq

 */

import Navbar from "./Navbar";

/**
 * The Layout component is the top level component of the application.           
 * It contains the Navbar and the main content.           
 * @param {React.ReactNode} children - The children of the layout.           
 * @returns A React functional component that is the layout for the application.      
 */
export default function Layout({ children }) {
	return (
		<>
			<div className="pageContainer">
				<Navbar />
				<main>{children}</main>
			</div>
		</>
	);
}
