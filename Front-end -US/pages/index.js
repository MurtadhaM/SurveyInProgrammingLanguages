/**
  * @author Murtadha Marzouq

 */

import LoadingScreen from "../components/LoadingScreen";
import Image from "next/image";
import { BsLinkedin, BsGithub } from "react-icons/bs";
import { CgFileDocument } from "react-icons/cg";

/**
 * The home page of the site.
 */
export default function Home() {
	return (
		<div>
			<div className="chart">
				<LoadingScreen />
			</div>
			<div className="container">
				<div className="behind-scenes">
					<div className="big title accent">
						<u>Behind the scenes</u>
					</div>
					<div>
						Ryan implemented the front end of the assignment, from designing the
						pages to the implementation of features and functionality. Ryan also
						parsed the data form the backend, to a usable format for charting,
						which he implemented and styled. Seth also worked on the front end,
						gathering data and information about our project and team, and
						implemented the documentation and sections here and below. Murtadha
						was repsonsible for making sure the data was scraped from the UNCC
						sites for the faculty, which Ryan later added to with scraped data
						from Google Scholar. We used Next.js as our framework for the front
						end, and Apache Echarts for the charting library. Our data is stored
						staticly as a JSON on GitHub.
						<br></br>
						Willis and Miguel worked on the backend of the project and created a
						document explaining everything we did, our user stories, and created
						nice diagrams showing our work. With their explanation of every
						detail, we hope everone can see the work and effort involved in our
						project.
					</div>
				</div>
				<div className="team-container">
					<div className="big title accent">
						<u>Meet the team</u>
					</div>

					<div className="team">
						<div className="team-member">
							<Image
								src="/TeamPhotos/Ryan_Hull.jpeg"
								alt="Ryan Hull"
								width="300"
								height="300"
								objectFit="cover"
							></Image>
							<div>
								<strong>Ryan Hull</strong> is a Senior graduating in May here at
								UNC Charlotte, with a BS in Computer Science, concentrating in
								Software, Systems & Networks. While born in Rochester, NY, Ryan
								has lived in Charlotte for most of his life and calls it home.
								Having experience in many technologies, from C++, Java, and
								Python, to Web Development (JavaScript, Angular, React, etc.),
								Ryan never passes up the opportunity to learn something new and
								expand his experience.
							</div>
							<div className="links">
								<a href="https://github.com/HullRyan">
									<BsGithub size={32} />
								</a>
								<a href="https://www.linkedin.com/in/ryan-hull-478b64178/">
									<BsLinkedin size={32} />
								</a>
								<a href="https://hullryan.github.io/">
									<CgFileDocument size={32} />
								</a>
							</div>
						</div>
						<div className="team-member">
							<Image
								src="/TeamPhotos/Murtadha_Marzouq.png"
								alt="Abu"
								width="300"
								height="300"
								objectFit="cover"
							></Image>
							<div>
								<strong>Murtadha Marzouq (Abu)</strong> is a graduate student
								with a concentration in Software, Systems and Networks at UNCC,
								where he also received his undergraduate degree. Abu is a
								professional IT specialist with more than 8 years of experience
								in IT infrastructure and networking. Abu attended Central
								Piedmont College before enrolling at the University of North
								Carolina in Charlotte. Murtadha provides IT help to our
								Charlotte, NC clients. He has built up IT infrastructure ranging
								from Cisco networking to Active Directory. He also knows Linux
								and how to set up Linux-based services like Secure FTP, MySQL,
								and the Apache web server. Murtadha was born in Syria and has
								lived in the United States for the past ten years.
							</div>
							<div className="links">
								<a href="https://webpages.charlotte.edu/mmarzouq/English/Resume.pdf">
									<CgFileDocument size={32} />
								</a>
							</div>
						</div>

						<div className="team-member">
							<Image
								src="/TeamPhotos/seth_adams.jpg"
								alt="Seth"
								width="300"
								height="300"
								objectFit="cover"
							></Image>
							<div>
								<strong>Seth Adams</strong> has been studying IT for over 6
								years from late high school to the present. Seth is working
								towards his degree in Computer Science with a concentration in
								Software, Systems & Networks. He started his studies at
								Rowan-Cabarrus Community College and transferred to UNCC last
								year. His experience in computer science includes not only his
								work at the university, but also a summer internship at TIAA
								over last summer. Seth was born and raised in San Antonio, Texas
								and has been living in Charlotte, North Carolina for 8 years.
							</div>
						</div>

						<div className="team-member">
							<Image
								src="/TeamPhotos/miguel.png"
								alt="miguel"
								width="300"
								height="300"
								objectFit="cover"
							></Image>
							<div>
								<strong>Miguel Morel</strong> is a Software Enthusiast with over
								4 years of experience in the Software Development scene. Miguel
								transferred from Central Piedmont Community College to the
								University of North Carolina at Charlotte (UNCC) for the last
								two years of his degree. He majors in Computer Science with a
								concentration in Software Engineering and is graduating in July
								2021. He is a skilled Software Developer with considerable skill
								in languages such as Java, C++, Python, JavaScript and SQL, to
								name a few. In his spare time, Miguel enjoys playing soccer and
								learning about emerging technologies and gadgets.
							</div>
							<div className="links">
								<a href="https://github.com/mmorel1">
									<BsGithub size={32} />
								</a>
								<a href="https://www.linkedin.com/in/miguelmorel94/">
									<BsLinkedin size={32} />
								</a>
							</div>
						</div>

						<div className="team-member">
							<Image
								src="/TeamPhotos/willis.jpg"
								alt="willis"
								width="300"
								height="300"
								objectFit="cover"
							></Image>
							<div>
								<strong>Willis Reid</strong>, I am currently a student at the
								University of North Carolina at Charlotte. Some of the things
								I&apos;ve done are graduated from Catawba Valley Community
								College with an associate degree. I have six years of experience
								working in customer service. Over the years, I have improved my
								problem-solving and critical thinking skills. I have also been
								studying IT for about five years now. I have experience with
								Python, HTML, and CSS.
							</div>
						</div>
					</div>
				</div>
				<br></br>
				<br></br>

				<style jsx>
					{`
						.team {
							display: flex;
							flex-wrap: wrap;
							justify-content: space-between;
							gap: 2rem;
						}
						.team-member {
							max-width: 300px;
							display: flex;
							gap: 1rem;
							flex-direction: column;
							padding: 1rem;
							background-color: var(--color-third);
						}
						.links {
							width: 100%;
							display: flex;
							justify-content: center;
							gap: 2rem;
						}
						.links > a {
							height: 2rem;
							width: 2rem;
						}
						.links > a:hover {
							color: var(--color-accent);
						}
						.container {
							display: flex;
							flex-direction: column;
							gap: 2rem;
						}
					`}
				</style>
			</div>
		</div>
	);
}
