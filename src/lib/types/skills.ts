export interface Skill {
    id: number
    name: string
    icones: string
}

export interface Skills {
    id: number
    name: string
    skills: Skills[]
}