export interface Skill {
    id: number
    name: string
    icones: string
}

export interface Skills {
	[x: string]: string | null | undefined;
    id: number
    name: string
    skills: Skills[]
}