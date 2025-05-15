export type Bookmark = {
    id: number;
    user: number;
    name: string;
    link: string;
    description: string;
    status: "alive" | "redirected" | "dead";
    created: string;
    workspaces: { id: number; name: string }[];
    tags: { id: number; name: string }[];
};
