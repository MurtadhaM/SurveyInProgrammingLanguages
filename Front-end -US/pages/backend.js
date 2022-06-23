/* eslint-disable @next/next/no-img-element */
/**
  * @author Murtadha Marzouq

 */

import Image from "next/image";

export default function Backend() {
	return (
		<>
			<div className="video-container">
				<div className="big title accent">Project Pitch</div>
				<iframe
					src="https://drive.google.com/file/d/1nGjPX7u8r3OY_AMT5IP31lIt9AH--S8P/preview"
					width="640"
					height="480"
					allow="autoplay"
				></iframe>
			</div>
			<div className="big title accent text">Document</div>
			<div className="backend-container">
				<iframe
					src="https://drive.google.com/file/d/1036be-M_JZcKqpo__k-AeRSHPlGvPP7N/preview"
					width="100%"
					height="100%"
					allow="autoplay"
				></iframe>
			</div>

			<div className="text">
				<p>
					*Written by <u>Miguel Morel</u> & <u>Willis Reid</u>
				</p>
			</div>

			<style jsx>
				{`
					.video-container {
						display: flex;
						flex-direction: column;
						justify-content: center;
						align-items: center;
						margin-top: 20px;
						margin-bottom: 20px;
						margin-left: auto;
						margin-right: auto;
					}
					.video-container iframe {
						max-width: 100%;
						
					}
					.backend-container {
						height: 70%;
						max-width: 1200px;
						overflow: none;
						margin-left: auto;
						margin-right: auto;
						margin-bottom: 20px;
						overflow: none;
					}
					.text {
						display: flex;
						justify-content: center;
						align-items: center;
						justify-content: center;
					}
				`}
			</style>
		</>
	);
}
